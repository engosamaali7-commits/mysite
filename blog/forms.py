from django import forms
# from blog import admin


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)
    
    
# from .models import Comment, Post
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#         list_display = ['name', 'email', 'post', 'created', 'active']
#         list_filter = ['active', 'created', 'updated']
#         search_fields = ['name', 'email', 'body']
