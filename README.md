## Описание
Проект представляет собой телеграм-бота для генерации анекдотов с использованием языковых моделей.

## Датасет
 Модель обучалась на датасете [Russian Jokes](https://www.kaggle.com/datasets/konstantinalbul/russian-jokes) и [собственном датасете](https://www.kaggle.com/datasets/maximovayana/vk-russian-joks), созданном путем парсинга 10 крупнейших ВК-пабликов с анекдотами.

 ## Эксперименты
- **experiments/** – ноутбуки с процессом подготовки данных и обучения моделей:
  - `vk_pablick_parser.ipynb` – парсинг данных и их предобработка  
  - `stat-llm.ipynb` – обучение модели на обработанных данных  
  - `gpt2-tuning.ipynb` – дообучение GPT-2 с использованием LoRA
    
## Загрузка предобученной модели
Чтобы запустить код предварительно необходимо [скачать](https://drive.google.com/drive/folders/120zUulvm85g1vudkQzn_f1z-x14_JVZ9?usp=sharing) модель и токенайзер и добавить файлы в папку models/stat_lm.
