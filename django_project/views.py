from django.shortcuts import render
import openai
import os

from .forms import AnswerForm

openai.api_key = os.environ['OPENAI']

# AI message generator
def generate_message(request, prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    messages=[
          {"role": "user", "content": f"Give me a Biblical answer to this question with a Bible reference: {prompt}"}
      ]
    )
    return response['choices'][0]['message']['content']

# Main page
def index(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            question= form['prompt'].value()
            message = generate_message(request, form['prompt'].value())
            context = {
              'question': question,
              'message': message,
            }
        return render(request, 'answer.html', context)
    else:
        form = AnswerForm()

    return render(request, "kist.html", {"form": form})