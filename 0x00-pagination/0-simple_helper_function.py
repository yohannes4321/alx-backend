def index_range(page,page_size):
    # start index
    # end index
    start_index=(page-1)*page_size
    end_index=page*page_size
    return start_index,end_index
