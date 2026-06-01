from dataclasses import dataclass

from django.shortcuts import render

# Create your views here.


@dataclass
class BlogPost:
    title: str
    content: str


def blog_list(request):

    print(request.method)
    print(request.headers)
    print(request)
    blogs = [
        BlogPost(title="First Post", content="This is the first blog post."),
        BlogPost(title="Second Post", content="This is the second blog post."),
        BlogPost(title="Third Post", content="This is the third blog post."),
    ]
    return render(request, "blog/blog_list.html", {"blogs": blogs})
