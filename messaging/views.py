from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView
from .models import Message

@method_decorator(login_required, name='dispatch')
class InboxView(ListView):
    model = Message
    template_name = 'messaging/inbox.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user)

@method_decorator(login_required, name='dispatch')
class SendMessageView(CreateView):
    model = Message
    fields = ['receiver', 'content']
    template_name = 'messaging/send_message.html'
    success_url = '/messaging/inbox/'

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)
