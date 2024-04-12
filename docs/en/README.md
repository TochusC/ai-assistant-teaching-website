<div align="center">
<h1> Intelligent Teaching Assistant Platform Empowered by AI 💯</h1>

An intelligent teaching assistant platform supporting **natural language interaction**

[![madewithlove](https://img.shields.io/badge/made_with-%E2%9D%A4-red?style=for-the-badge&labelColor=orange)](https://github.com/TochusC/ai-assistant-teaching-website)

[**简体中文**](./README.md) | [**English**](./../en/README.md) | [**日本語**](./../jp/README.md)

</div>

---

## Intelligent Teaching Assistant Platform with Vue3 + Unity(WebGL) 📚
![example.png](../example_image/example.png)
***
### Phase completion, construction temporarily paused 🛠️...
***

Utilizing a large language model as your personal assistant, let (him/her/it) assist you in navigating the teaching platform, querying teaching information, summarizing webpage content, solving your difficulties, fulfilling your requests, and even engaging in casual conversation, exchanging affections, and more!

***
### Introducing a New Web Interaction Logic 👾!
No more clicking through various webpage items and navigation menus with a mouse; no more learning complex webpage business logic and operations; no more analyzing cold and rigid chart data displays.
#### Operate webpages through text and voice in a natural language ✨!
Through text or voice communication with the intelligent teaching assistant, it will help you navigate to the corresponding webpage modules, assist you in summarizing webpage content, analyzing chart data, and help you navigate the teaching platform smoothly to complete teaching tasks.
### Real-time Feedback from the Large Model, Customized Learning Assessment 🌟!
***
### Meet Your Intelligent Teaching Assistant — Xiao Hui ❤️!

Through technologies such as Speech-to-Text (STT), a large language model (LLM), Text-to-Speech (TTS), etc.,
we have created the intelligent teaching assistant Xiao Hui and introduce her to you 🥰.

<div align="center">

![example_0.png](../example_image/example_0.png)

</div>

Don't want to learn the complex business logic of the teaching platform? No problem!

~~Let Xiao Hui help students submit assignments, complete tasks; help teachers take attendance, assign homework, and other tedious operations.~~

Unfortunately, at present, Xiao Hui can only perform routing navigation, but functions such as assigning homework, querying backend data, filling out forms, etc., are **theoretically feasible**.

For any task, just say a word to Xiao Hui, and she will do her best to fulfill your needs!

***
##### Speech-to-Text (STT) is implemented using Baidu's Rapid Phrase Speech Recognition Service
##### Large Language Model (LMM) is Baidu's ERNIE 3.5
##### ~~Text-to-Speech (TTS) is implemented through the GitHub project [GPT-SoVits](https://github.com/RVC-Boss/GPT-SoVITS)~~
##### Text-to-Speech (TTS) is implemented through Baidu's short text-to-speech synthesis service (speaker is per6-Du Xiao Meng)


### Platform Preview❓

---
#### Website Homepage
![example_1.png](../example_image/example_1.png)

#### Learning Progress Assessment
![example_2.png](../example_image/example_2.png)

#### Personalized Learning Plan Generation
![example_3.png](../example_image/example_3.png)

#### My School Page (Dark Mode)
![example_3.png](../example_image/example_3.png)


### Run the Project 🚀:
#### Environment Setup 🔨:
***

The project uses Node.js v18.18.0 as the runtime environment and is developed using the Vue3 framework.

The frontend uses [Naive UI](https://www.naiveui.com/), [Element-Plus](https://element-plus.org/) component libraries.
It also includes three-dimensional interactive models implemented through [Spline](https://spline.design/).

The backend uses Django as the server-side framework. The project has three backend services, all located in the `/affiliate-project` directory.

They are:
- AvatarServer, the virtual assistant server responsible for calling Baidu's speech recognition service, large language model service, and Baidu's speech synthesis service.
- backend, the data server using SQLite database, responsible for storing website backend data, including user information, course information, homework information, etc.
- cdn, the static file server responsible for storing the website's static files, including images, audio, video, etc.

Before running the project, please use:
```shell
npm install
```

to install the required libraries and dependencies specified in package.json.

Then start the three backend services separately:

Navigate to the AvatarServer, backend, cdn directories under the `/affiliate-project` directory,

#### Before running the Django backend,
make sure you have installed Python and the necessary libraries, 
such as Django, Requests, etc. 
Refer to the `requirements.txt` and `readme.md` files in each backend.

Run the `run.bat` file in each directory to start the corresponding backend service.

Finally, use
```shell
npm run dev
```

to start the frontend project.

Enjoy 😉!

### Notes ❗:

---
The intelligent virtual assistant Xiao Hui can assist users in routing navigation by describing your needs in natural language. Xiao Hui will help you complete the navigation.

Please refer to the `/src/components/UnityInteraction.vue` file for the specific implementation process.

Apart from the virtual teaching assistant Xiao Hui, there are no other highlights in the project.

We have implemented the virtual character Xiao Hui in the `/src/components/UnityComponent.vue component`. Welcome everyone to discuss together 🤗.