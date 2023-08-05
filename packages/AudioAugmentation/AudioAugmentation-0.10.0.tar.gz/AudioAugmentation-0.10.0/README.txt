# AudioAugmentation
 Libreria python para aumentar audios haciendo transformaciones sobre los audios, 
 de esta manera mediante algunas transformaciones sobre los audios se recibe un audio y se multiplica por 9 salidas
 
## Initialization

```bash
pip install AudioAugmentation
```

A `AudioAugmentation` object should be created and use its attributes.

```python
from AudioAugmentation import Audio_K
aumentedAudio = Audio_K(audio_file=file_path, save=save, graph=grafica)
todos_audios = aumentedAudio.aumentar()
```

### Audio_K methods

* `aumentar()`: returns all transforms about a audio, you can save the new audios o only show

