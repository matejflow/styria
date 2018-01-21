from collections import deque

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class Pagination():
    """
    Return Paginator object given QuerySet
    """

    def __init__(self, query_set, paginate_by, page):
        self.set = query_set
        self.paginate_by = paginate_by or 5
        self.page = page or 1

    def list_next(self, objects, max=0):
        next_list = deque()
        counter = 1
        if max:
            max_pages = objects.number + max
            if max_pages > objects.paginator.num_pages:
                max_pages = objects.paginator.num_pages
        else:
            max_pages = objects.paginator.num_pages

        if objects.has_next:
            for i in range(objects.number+1, max_pages+1):
                counter += 1
                next_list.append(i)
                if counter >= 5:
                    break
            objects.page_range += next_list
            return objects
        else:
            return objects

    def list_previous(self, objects, min=0):
        previous_list = deque()
        counter = 1
        min_pages = min
        if not min:
            min_pages = objects.paginator.num_pages-4
        else:
            min_pages = objects.number-min

        for i in range(min_pages, objects.number):
            counter += 1
            if i > 0:
                previous_list.append(i)
            if counter >= 5:
                break
        objects.page_range += previous_list
        return objects

    def list_all(self, objects):
        """
        Calculates list for has_previous and has_next case
        """
        dif_prev = objects.number - 1
        dif_next = objects.paginator.num_pages - objects.number

        if dif_prev >= 2 and dif_next >= 2:
            objects = self.list_previous(objects, 2)
            objects = self.list_next(objects, 2)
        elif dif_prev < 2 and dif_next >= 2:
            objects = self.list_previous(objects, 1)
            objects = self.list_next(objects, 3)
        elif dif_prev >= 2 and dif_next < 2:
            objects = self.list_previous(objects, 3)
            objects = self.list_next(objects, 1)
        else:
            objects = self.list_previous(objects)
            objects = self.list_next(objects)
        return objects

    def show_nice_pagination(self, objects):
        setattr(objects, 'page_range', [int(self.page)])
        if not objects.has_previous():
            return self.list_next(objects)
        elif not objects.has_next():
            return self.list_previous(objects)
        else:
            return self.list_all(objects)

    def list(self):
        paginator = Paginator(self.set, self.paginate_by)
        try:
            object_list = paginator.page(self.page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        object_list = self.show_nice_pagination(object_list)
        object_list.page_range.sort()
        return object_list
