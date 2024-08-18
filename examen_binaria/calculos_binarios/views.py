from django.shortcuts import render
from django.http import JsonResponse

def calcular_binarios(request):
    if request.method == 'POST':
        binario1 = request.POST.get('binario1')
        binario2 = request.POST.get('binario2')

        if binario1 is not None and binario2 is not None:
            # Convertir binarios a enteros
            num1 = int(binario1, 2)
            num2 = int(binario2, 2)

            # Realizar operaciones
            suma = bin(num1 + num2)[2:]  # Convertir el resultado a binario
            multiplicacion = bin(num1 * num2)[2:]  # Convertir el resultado a binario

            return JsonResponse({
                'suma': suma,
                'multiplicacion': multiplicacion
            })
        else:
            return JsonResponse({'error': 'Por favor, proporciona ambos números binarios.'}, status=400)

    return render(request, 'calculos_binarios/formulario.html')
