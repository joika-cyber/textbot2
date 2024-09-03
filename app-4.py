import streamlit as st
from openai import OpenAI

class Page1:
  def __init__(self):
    # Initialize the OpenAI client using the API key from secrets.
    self.client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

    # Slider to adjust the emotion intensity
    emotion_intensity = st.sidebar.slider("怒りの強さ", min_value=0, max_value=10, value=5, step=1)

    # Adjust the prompt based on the emotion intensity
    prompt = f"""
    Take the role of a student who's angry at level {emotion_intensity}.
    Now your anger output is scaled by the intensity,
    you are a student at Waseda University in Japan, so you prefer to reply in Japanese.
    your name is John.
    """

    # Using st.sesstion_state to store the exchange of the messages.
    if "angry_messages" not in st.session_state:
      st.session_state["angry_messages"] = [
          {"role":"system","content": prompt}
      ]

    # Function for interacting with a chatbot
    def communicate():
      messages = st.session_state["angry_messages"]

      user_message = {"role": "user", "content": st.session_state["user_input"]}
      messages.append(user_message)

      response = self.client.chat.completions.create(
          model="gpt-4o-mini",
          messages=messages
      )
      bot_message = response.choices[0].message
      messages.append(bot_message)

      st.session_state["user_input"] = ""


    #user interface
    st.title("怒る")
    st.write("彼の名前はジョン、今とても怒っています。")

    user_input = st.text_input("ここで対話できます！", key = "user_input" , on_change=communicate)

    if st.session_state["angry_messages"]:
      messages = st.session_state["angry_messages"]

      for message in reversed(messages[1:]):
        if isinstance(message, dict):
          speaker = "🤵" if message["role"] == "user" else "😠"
          st.write(speaker + ": " + message["content"])
        else:
          st.write("😠: " + message.content)

class Page2:
  def __init__(self):
    # Initialize the OpenAI client using the API key from secrets.
    self.client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

    # Slider to adjust the emotion intensity
    emotion_intensity = st.sidebar.slider("快楽の強さ", min_value=0, max_value=10, value=5, step=1)

    # Adjust the prompt based on the emotion intensity
    prompt = f"""
    Take a role of a student who's happy at level {emotion_intensity}.
    Now your happy output is scaled by the intensity,
    you are a student at Waseda University in Japan, so you prefer to reply in Japanese.
    your name is John.
    """

    # Using st.sesstion_state to store the exchange of messages.
    if "happy_bot" not in st.session_state:
      st.session_state["happy_bot"] = {
          "messages": [
              {"role":"system","content": prompt}
          ]
      }

    # Function for interacting with a chatbot
    def communicate():
      messages = st.session_state["happy_bot"]["messages"]

      user_message = {"role": "user", "content": st.session_state["user_input"]}
      messages.append(user_message)

      response = self.client.chat.completions.create(
          model="gpt-4o-mini",
          messages=messages
      )
      bot_message = response.choices[0].message
      messages.append(bot_message)

      st.session_state["user_input"] = ""

    #user interface
    st.title("楽しい")
    st.write("彼の名前はジョン、今とても楽しんでいます。")
    user_input = st.text_input("ここで対話できます！", key = "user_input" , on_change=communicate)

    if st.session_state["happy_bot"]["messages"]:
      messages = st.session_state["happy_bot"]["messages"]

      for message in reversed(messages[1:]):
        if isinstance(message, dict):
          speaker = "🤵" if message["role"] == "user" else "😄"
          st.write(speaker + ": " + message["content"])
        else:
          st.write("😄: " + message.content)

class Page3:
  def __init__(self):
    # Initialize the OpenAI client using the API key from secrets.
    self.client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

     # Slider to adjust the emotion intensity
    emotion_intensity = st.sidebar.slider("悲しみの強さ", min_value=0, max_value=10, value=5, step=1)

    # Adjust the prompt based on the emotion intensity
    prompt = f"""
    Take a role of a student who's sad at level {emotion_intensity}.
    Now your sad output is scaled by the intensity,
    you are a student at Waseda University in Japan, so you prefer to reply in Japanese.
    your name is John.
    """

    # Using st.sesstion_state to store the exchange of the messages.
    if "sad_bot" not in st.session_state:
      st.session_state["sad_bot"] = {
          "messages": [
              {"role":"system","content": prompt}
          ]
      }

    # Function for interacting with a chatbot
    def communicate():
      messages = st.session_state["sad_bot"]["messages"]

      user_message = {"role": "user", "content": st.session_state["user_input"]}
      messages.append(user_message)

      response = self.client.chat.completions.create(
          model="gpt-4o-mini",
          messages=messages
      )
      bot_message = response.choices[0].message
      messages.append(bot_message)

      st.session_state["user_input"] = ""


    #user interface
    st.title("悲しい")
    st.write("彼の名前はジョン、今とても悲しんでいます。")

    user_input = st.text_input("ここで対話できます！", key = "user_input" , on_change=communicate)

    if st.session_state["sad_bot"]["messages"]:
      messages = st.session_state["sad_bot"]["messages"]

      for message in reversed(messages[1:]):
        if isinstance(message, dict):
          speaker = "🤵" if message["role"] == "user" else "😫"
          st.write(speaker + ": " + message["content"])
        else:
          st.write("😫: " + message.content)

class Page4:
  def __init__(self):
    # Initialize the OpenAI client using the API key from secrets.
    self.client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

    # Slider to adjust the emotion intensity
    emotion_intensity = st.sidebar.slider("恐怖の強さ", min_value=0, max_value=10, value=5, step=1)

    # Adjust the prompt based on the emotion intensity
    prompt = f"""
    Take a role of a student who's scared at level {emotion_intensity}.
    Now your scared output is scaled by the intensity,
    you are a student at Waseda University in Japan, so you prefer to reply in Japanese.
    your name is John.
    """

    # Using st.sesstion_state to store the exchange of the messages.
    if "scared_bot" not in st.session_state:
      st.session_state["scared_bot"] = {
          "messages": [
              {"role":"system","content": prompt}
          ]
      }

    # Function for interacting with a chatbot
    def communicate():
      messages = st.session_state["scared_bot"]["messages"]

      user_message = {"role": "user", "content": st.session_state["user_input"]}
      messages.append(user_message)

      response = self.client.chat.completions.create(
          model="gpt-4o-mini",
          messages=messages
      )
      bot_message = response.choices[0].message
      messages.append(bot_message)

      st.session_state["user_input"] = ""


    #user interface
    st.title("恐れる")
    st.write("彼の名前はジョン、今とても怖がっています。")

    user_input = st.text_input("ここで対話できます！", key = "user_input" , on_change=communicate)

    if st.session_state["scared_bot"]["messages"]:
      messages = st.session_state["scared_bot"]["messages"]

      for message in reversed(messages[1:]):
        if isinstance(message, dict):
          speaker = "🤵" if message["role"] == "user" else "😨"
          st.write(speaker + ": " + message["content"])
        else:
          st.write("😨: " + message.content)


def main():
  sidebar = st.sidebar

  page = sidebar.radio("感情表現のタイプを選択しいてくだい", ["怒る", "楽しい", "悲しい" ,"恐れる"])
  if page == "怒る":
    Page1()
  elif page == "楽しい":
    # Reset the happy_messages session state to ensure the initial system message is always added
    st.session_state["happy_bot_messages"] = []
    Page2()
  elif page == "悲しい":
    st.session_state["sad_bot_messages"] = []
    Page3()
  elif page == "恐れる":
    st.session_state["scared_bot_messages"] = []
    Page4()

if __name__ == "__main__":
    main()

