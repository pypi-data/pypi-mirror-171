# Explain Me

# Example
```
from explain_me.visual import visualize_package





with open('preview.html', 'w+') as file:
    file.write("""
<html>
    <body>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <script>
            mermaid.initialize({ startOnLoad: true });
            
            
//get svg element.
var svg = document.getElementsByTagName('svg')[0];

            
            
        </script>

        <div class="mermaid">
            classDiagram
    """)
    

    for line in visualize_package(nama_library):
        file.write(line+"\n")

    file.write("""
            
        </div>
        <a id="link" href="#">download</a>
    </body>
</html>
        """)
```