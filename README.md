## Description
Your assignment this week is to convert the function-based views in your blogging app into class-based views. Your work will be very similar to the work we did in the lesson content to create the polling class-based views, except:

- The blogging detail view doesn't accept POST requests, so there will be no need to create a `post` method in the blogging detail view.
- When you're done, the front page should continue to display only published posts and it should continue to display posts in reverse-chronological order. 
To accomplish this, you'll be providing a `queryset` class attribute in your list view instead of a `model` class attribute. \
See https://docs.djangoproject.com/en/2.1/topics/class-based-views/generic-display/#viewing-subsets-of-objectsLinks to an external site. 
- for examples of filtering and sorting querysets. You'll want to apply both `filter` (or `exclude`) and `order_by` methods to your `Post.objects` queryset.

The examples in the documentation use a `context_object_name` variable, but I would _not_ use that in your homework.

### Submitting Your Work 
1. This assignment does not have a GitHub Classrooms component.
1. Click the Submit Assignment button in the upper right.
1. Create a zip archive of the directory for this project.
1. Use the Choose File button to find and select the .zip file.
1. Click the Submit Assignment button.
1. In a comment, please also provide a link to your blog repository, on GitHub.