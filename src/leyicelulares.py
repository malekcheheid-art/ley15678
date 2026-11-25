"""Act10 - Laboratorio de Programacion (LPR 5o Ano) - E.E.S.T. N. 100
ACTIVIDAD 10 BIS - Simulador de Normativa de Celulares en el Aula (Ley 15.678)
DOCENTE: Mansilla Munoz York Elxas
ESTUDIANTE: [TU APELLIDO Y NOMBRE - COMPLETAR OBLIGATORIAMENTE]
"""

print("##################################################")
print("### SISTEMA DE ASESORAMIENTO NORMATIVO ESCOLAR ###")
print("##################################################\n")

# Simulamos las variables de contexto del aula
autorizacion_docente = False   # Cambiar a True si el profe habilito la actividad digital
emergencia_familiar = False    # Cambiar a True si fue validado por preceptores

print(f"Estado de Autorizacion Docente   {autorizacion_docente}")
print(f"Estado de Emergencia Validada    {emergencia_familiar}\n")

# Estructura de decision
if autorizacion_docente == True:
    print("[ACCESO PERMITIDO] El celular solo para estudiar y para aprender (Fines Pedagogicos).")
elif emergencia_familiar == True:
    print("[CANALIZACION INSTITUCIONAL] Gestionar la comunicacion urgente a traves de preceptor/a y/o direccion.")
else:
    print("[RESTRICCION LEY 15.678] Tu celular debe permanecer guardado en la mochila.")

print("##################################################")
