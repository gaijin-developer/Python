contents = ["All carrots are to be sliced ", "the shape of the world is round",
            "the ui of the landing page need some contrast fixing"]
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(f"../Files/{filename}", "w")
    file.write(content)
