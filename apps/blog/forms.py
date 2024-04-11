from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    """Форма для добавления постов."""

    class Meta:
        model = Post
        fields = (
            'thumbnail',
            'title',
            'description',
            'text',
            'category',
        )

    def __init__(self, *args, **kwargs):
        """Обновление стилей в форме."""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off',
            })


class PostUpdateForm(PostCreateForm):
    """Форма для обновления поста."""

    class Meta:
        model = PostCreateForm.Meta.model
        fields = PostCreateForm.Meta.fields + ('fixed',)

    def __init__(self, *args, **kwargs):
        """Обновление стилей в форме."""
        super().__init__(*args, **kwargs)
        self.fields['fixed'].widget.attrs.update({
            'class': 'form-check-input'
        })