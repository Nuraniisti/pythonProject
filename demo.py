import gradio as gr

def greet(name, intensity):
    return "Hello " * intensity + name + "!"

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
    title="Hello, world",
    description="This is simple hello word application using gradio",
    article="This is article. Put some text here."
)

demo.launch()