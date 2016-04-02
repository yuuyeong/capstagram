from tags.models import Tag


def get_tag_list(content):
    tag_list = [
        word.replace("#", "")
        for word
        in content.split(" ")
        if word.startswith("#")
    ]

    return tag_list


def get_tagify_content(content):
    tag_list = get_tag_list(content)

    word_list = [
        word
        for word
        in content.split(" ")
    ]

    tagified_word_list = []

    for word in word_list:
        if word in ["#{name}".format(name=tag) for tag in tag_list]:
            word = "<a href='{tag_url}'>{tag_name}</a>".format(
                tag_url=Tag.objects.get(name=word.replace("#", "")).get_absolute_url(),
                tag_name=word,
            )
        tagified_word_list.append(word)

    return " ".join(tagified_word_list)
