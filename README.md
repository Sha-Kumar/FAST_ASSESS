# FAST_ASSESS

### Built With

- [Fastapi](https://github.com/tiangolo/fastapi)
- [Python](https://www.python.org/)
- [OpenCV](https://aws.amazon.com/)
- [AWS](https://pypi.org/project/opencv-python/)

## Getting Started

### Prerequisites

Command to install all the requirements required for the project to run in our case we have created requirements.txt file you can also create your own requirements :

```sh
pip install -r requirements.txt
```

Command to run the API :

```sh
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
```
After the command is executed it will start the server.
Now open the Chrome (or any) browser.

The test API :

```
http://127.0.0.1:8000/test
```

The API to capture images :

```
http://127.0.0.1:8000/upload-images/
```

## License

This project is licensed under the **MIT license**. Feel free to edit and distribute this template as you like.

See [LICENSE](LICENSE) for more information.
