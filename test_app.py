import sys
from unittest.mock import patch, MagicMock


def _reload_app():
    if "app" in sys.modules:
        del sys.modules["app"]


@patch("streamlit.text_input")
@patch("streamlit.write")
@patch("langchain_groq.ChatGroq")
@patch("langgraph.prebuilt.create_react_agent")
def test_app_initializes_model_with_correct_params(
    mock_create_agent,
    mock_chat_groq,
    mock_write,
    mock_text_input,
):
    mock_text_input.return_value = ""
    _reload_app()

    import app

    mock_chat_groq.assert_called_once_with(model="openai/gpt-oss-120b")


@patch("streamlit.text_input")
@patch("streamlit.write")
@patch("langchain_groq.ChatGroq")
@patch("langgraph.prebuilt.create_react_agent")
def test_app_creates_agent_with_model(
    mock_create_agent,
    mock_chat_groq,
    mock_write,
    mock_text_input,
):
    mock_text_input.return_value = ""
    mock_model = MagicMock()
    mock_chat_groq.return_value = mock_model
    _reload_app()

    import app

    mock_create_agent.assert_called_once_with(model=mock_model, tools=[])


@patch("streamlit.text_input")
@patch("streamlit.write")
@patch("langchain_groq.ChatGroq")
@patch("langgraph.prebuilt.create_react_agent")
def test_app_invokes_agent_on_user_input(
    mock_create_agent,
    mock_chat_groq,
    mock_write,
    mock_text_input,
):
    mock_text_input.return_value = "test question"
    mock_agent = MagicMock()
    mock_agent.invoke.return_value = {
        "messages": [MagicMock(content="test answer")]
    }
    mock_create_agent.return_value = mock_agent
    _reload_app()

    import app

    mock_agent.invoke.assert_called_once_with(
        {"messages": [{"role": "user", "content": "test question"}]}
    )


@patch("streamlit.text_input")
@patch("streamlit.write")
@patch("langchain_groq.ChatGroq")
@patch("langgraph.prebuilt.create_react_agent")
def test_app_displays_response(
    mock_create_agent,
    mock_chat_groq,
    mock_write,
    mock_text_input,
):
    mock_text_input.return_value = "test question"
    mock_agent = MagicMock()
    mock_agent.invoke.return_value = {
        "messages": [MagicMock(content="test answer")]
    }
    mock_create_agent.return_value = mock_agent
    _reload_app()

    import app

    mock_write.assert_called_once_with("test answer")
