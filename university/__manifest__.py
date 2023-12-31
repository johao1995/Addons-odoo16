{
    "name":"university_unfv",
    "description":"""
        Modulo para almacenar informacion de student
    """,
    "category":"Universidad",
    "author":"Johao Marcos Maldonado Roman",
    "version":"16.0.0.1",
    "depends":[
        "base",
        "mail"
    ],
    "data":[
        #data
        "data/department.xml",
        "data/grado.xml",
        "data/student_matricula.xml",
        #menu
        "views/teacher_view.xml",
        "views/student_view.xml",
        "views/department_view.xml",
        "views/asignatura_view.xml",
        "views/student_matricula_view.xml",
        "views/year_school.xml",
        "views/menu.xml",
        #security
        "security/res_groups.xml",
        "security/ir.model.access.csv"
    ],
    "installed":True
}