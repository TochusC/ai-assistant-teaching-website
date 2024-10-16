<div align="center">
<h1> AI-Powered Intelligent Teaching Assistant Platform💯</h1>

An intelligent teaching assistant platform supporting **natural language interaction**

[![madewithlove](https://img.shields.io/badge/made_with-%E2%9D%A4-red?style=for-the-badge&labelColor=orange)](https://github.com/TochusC/ai-assistant-teaching-website)

[**简体中文**](./README.md) | [**English**](./../en/README.md)

Congratulations to **AI Assistant - Xiaohui** for winning national awards in the following competitions👏:

[(16th) China College Students Computer Design Competition](https://jsjds.blcu.edu.cn/)-Software Application and Development Track-**National First Prize**

[13th "China Software Cup" College Students Software Design Competition](https://www.cnsoftbei.com/)-A5-Intelligent Education Application Software Development Track based on iFLYTEK AI Platform-**National Second Prize**

[2024 China College Students Computer Competition - Network Technology Challenge](http://net.c4best.cn/)-A1 Creative Track-**National Third Prize**



</div>

---

## Vue3 + Unity(WebGL) Intelligent Teaching Assistant Platform📚
![example.png](../example_image/example.png)
***
### Phase Completion, Construction Temporarily Halted🛠️...
***

Use large language models as your personal assistant to help you navigate the teaching platform, query teaching information, summarize web content, solve your problems, meet your needs, and even chat about anything!

***
### Offering a New Web Interaction Logic👾!
No more clicking through complex web items and navigation with a mouse; no more learning complicated web business logic and operations; no more analyzing cold, hard data from web charts.
#### Operate the web through text and voice using natural language✨!
Communicate with the intelligent teaching assistant through text or voice, and the assistant will help you navigate to the relevant web modules, summarize web content, analyze chart data, and assist you in seamlessly exploring the teaching platform and completing teaching tasks.
### Real-time Feedback from Large Models, Customized Learning Assessment🌟!
***
### Meet Your Intelligent Teaching Assistant - Xiaohui❤️!

Using technologies like Speech-to-Text (STT), Large Language Models (LLM), and Text-to-Speech (TTS),
we have created the intelligent teaching assistant Xiaohui and introduced her to you🥰.

<div align="center">
<img src="../example_image/example_0.png" width="auto" height="320px" />
</div>

Don't want to learn the complex business logic of the teaching platform? No problem!

~~Let Xiaohui help students submit assignments, complete tasks; help teachers with attendance and assignment operations.~~

Unfortunately, Xiaohui can currently only perform routing navigation, but functions like assignment submission, backend data querying, and form filling are **theoretically achievable**.

For any task, just say a word to Xiaohui, and she will go all out🔥 to meet your needs!

***
##### Speech-to-Text (STT) is implemented using Baidu's Short Speech Recognition Express Edition service
##### Large Language Model (LLM) is provided by Baidu's ERNIE 3.5
##### ~~Text-to-Speech (TTS) is implemented through the GitHub project [GPT-SoVits](https://github.com/RVC-Boss/GPT-SoVITS)~~
##### Text-to-Speech (TTS) is implemented through Baidu's Short Text-to-Speech synthesis (voice actor: per6-Du Xiaomeng)


### Platform Preview❓

---
#### Website Homepage

![example_1.png](../example_image/example_1.png)

#### Learning Progress Assessment
![example_2.png](../example_image/example_2.png)

#### Personalized Learning Plan Generation
![example_3.png](../example_image/example_3.png)

#### My Classroom Page (Dark Mode)
![example_3.png](../example_image/example_3.png)


### Running the Project🚀:
#### Environment Preparation🔨:
***

The project uses Node.js v18.18.0 as the runtime environment and is developed using the Vue3 framework.

The frontend uses [Naive UI](https://www.naiveui.com/) and [Element-Plus](https://element-plus.org/) component libraries.
Additionally, it includes 3D interactive models implemented through [Spline](https://spline.design/).

The backend uses Django as the server framework, with Python version 3.12.0. The project has three backend services located in the `/affiliate-project` directory.

They are:
- AvatarServer, the virtual human server, responsible for calling Baidu's speech recognition service, large language model service, and speech synthesis service.
- backend, the data server, using SQLite database, responsible for storing website backend data, including user information, course information, assignment information, etc.
- cdn, the static file server, responsible for storing website static files, including images, audio, video, etc.

Before running the project, please use:
```shell
npm install
```
to install the necessary libraries and dependencies listed in `package.json`.

Use
```shell
npm run dev
```
to start the frontend. You can then meet Xiaohui by visiting [http://127.0.0.1:5173/](http://127.0.0.1:5173/).

However, to enter the teaching website and let Xiaohui start working, you need to start the three backend services separately:

Navigate to the `AvatarServer`, `backend`, and `cdn` directories under `/affiliate-project`.

##### Before running the Django backend, please ensure you have installed Python and the necessary libraries such as Django, Requests, etc. Refer to the `requirements.txt` and `readme.md` files in each backend directory.

Run the `run.bat` file in each corresponding directory to start the backend services.

Enjoy😉!

### Notes❗:
***
The intelligent assistant Xiaohui can help users with routing navigation functions. Just describe your needs in natural language, and Xiaohui will help you navigate.

For the specific implementation process, please refer to the `/src/components/UnityInteraction.vue` file.

Apart from the virtual teaching assistant Xiaohui, there are no other highlights in the project.
The virtual assistant Xiaohui is implemented in the `/src/components/UnityComponent.vue` component. We welcome everyone to discuss and explore together🤗.div align="center">
