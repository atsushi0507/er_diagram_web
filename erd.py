from plantuml import PlantUML
import os

server = PlantUML(url='http://www.plantuml.com/plantuml/png/')
def generate_png(uml_code, file_name):
    output = server.processes(uml_code)

    os.makedirs("output", exist_ok=True)
    with open(f"output/{file_name}.png", "wb") as f:
        f.write(output)

uml = """
@startuml
top to bottom direction
skinparam linetype ortho

entity "Table1" as t1 {
    +id
    --
    name
}

entity "Tables2" as t2 {
    +id
    --
    quantity
}

entity "Table3" as t3 {
    +id
    --
    name
    quantity
}

t1 --> t3
t2 --> t3

@enduml
"""

generate_png(uml, "erd")
