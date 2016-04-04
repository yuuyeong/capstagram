def post_order_by(post_list):
    # queryset(글목록) -> order_by("-created_at") -> sort 후 return
    post_list = post_list.order_by("-created_at")
    return post_list
