# AIOUC: simulation of Ocean University of China's course selection system

Inspired by latest works in simulation using LLMs, this is a small script that simulates Ocean University of China's course selection process. We use Ollama to make decisions and simulate a simplified process.

Sounds like a cool idea, but it's still too simple and crude. Partly because the limitation of my knowledge, other partly because llama3.1 is not as smart as I thought.

# Run

Install Ollama using one command:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Get llama3.1 model by:

```
ollama run install llama3.1
```

Good news, this small project is developed using only standard Python libraries, no need to install any other packages.

Run the script:

```bash
python simulate.py
```

Parameters can be modified in `constants.py`

# Future works

- Enhance the simulation process maybe.
- Use better LLMs.
- Analyze the simulation in scripts (currently, the analyze process is done manually using the files stored in `./save`).