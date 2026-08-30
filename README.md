# Transcribe audios localmente
Este repositorio permite agarrar grabaciones realizadas y transcribirlas automáticamente utilizando un modelo de AI basado en `openai-whisper`

<img width="1131" height="644" alt="image" src="https://github.com/user-attachments/assets/d1c004b5-6233-455e-b4eb-5fc096750e07" />


## Como usarlo
### Paso 1: Clonar el repositorio

#### Crear una nueva carpeta (opcional)
```cmd
mkdir repositorio
```

#### Ingresar a la carpeta
```cmd
cd repositorio
```

#### Clonar este repositorio
```cmd
git clone https://github.com/ariasj07/transcribe-free/
```
#### Abrirlo
```cmd
cd transcribe-free
```
### Instalar dependencias
```cmd
pip install -r requirements.txt
```
## Usarlo para grabar
```python
python .\record.py
>>>
```
### Mantener presionado F9 para grabar
```cmd
>>> Grabando...
```
### Para terminar, simplementar soltar F9
```cmd
>>> Grabación finalizada
```
## Transcribir grabación
```python
python .\use_model.py
>>> <transcripción...>
```
