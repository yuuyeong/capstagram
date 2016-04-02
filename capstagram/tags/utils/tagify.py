def get_tag_list(instance):
    tag_list = [
        word.replace("#", "")
        for word
        in instance.content.split(" ")
        if word.startswith("#")
    ]

    return tag_list
