from rag.chatbot import load_data

def test_load_data(monkeypatch):
    expected = ["Directory"]
    args={}

    class FakeReader:
        def __init__(self,**kwargs):
            args.update(kwargs)

        def load_data(self):
            return ["Directory"]

    answers = iter(["d", "test_directory"])
    monkeypatch.setattr('builtins.input', lambda _: next(answers))
    monkeypatch.setattr('rag.chatbot.SimpleDirectoryReader', FakeReader)
    assert load_data() == expected
    assert args['input_dir'] == "test_directory"
    
