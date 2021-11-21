<!DOCTYPE html>
<html>
  <head>
    <title>Online Python Compiler (Interpreter)</title>
    <link
      rel="shortcut icon"
      href="https://cdn.programiz.com/sites/tutorial2program/files/programiz-favicon_3.png"
      type="image/png"
    />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, user-scalable=0"
    />
    <link rel="canonical" href="https://www.programiz.com/python-programming/online-compiler/" />    <meta
      name="description"
      content="Write and run Python code using our online compiler (interpreter). You can use Python Shell like IDLE, and take inputs from the user in our Python compiler."
    />

    <!-- CMP and header ad code start -->
    <script src="https://cmp.uniconsent.com/v2/stub.min.js"></script>
    <script async src='https://cmp.uniconsent.com/v2/a8d3ae4937/cmp.js'></script>
    <script type="text/javascript">
    window.googletag = window.googletag || {};
    window.googletag.cmd = window.googletag.cmd || [];
    window.googletag.cmd.push(function () {
        window.googletag.pubads().enableAsyncRendering();
        window.googletag.pubads().disableInitialLoad();
    });
    (adsbygoogle = window.adsbygoogle || []).pauseAdRequests = 1;
    </script>
    <script>
    __tcfapi("addEventListener", 2, function(tcData, success) {
        if (success && tcData.unicLoad  === true) {
            if(!window._initAds) {
                window._initAds = true;
                var script = document.createElement('script');
                script.async = true;
                script.src = '//dsh7ky7308k4b.cloudfront.net/publishers/Programizcomnew.min.js';
                document.head.appendChild(script);
            }

            try {
                fetch(new Request("https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js", { method: 'HEAD', mode: 'no-cors' })).then(function(response) {
            return true;
            }).catch(function(e) {
            document.getElementsByClassName("content-top-ad")[0].style.display = "none";
            var ad_elements = document.getElementsByClassName("pub-ad");
            while(ad_elements.length > 0){
                ad_elements[0].parentNode.removeChild(ad_elements[0]);
            }
            var carbonScript = document.createElement("script");
            carbonScript.src = "//cdn.carbonads.com/carbon.js?serve=CKYDL27L&placement=wwwprogramizcom";
            carbonScript.id = "_carbonads_js";
            document.getElementById("carbon-block").appendChild(carbonScript);

            });
        } catch (error) {
            console.log(error);
        }
        }
    });
    </script>
    <!-- CMP and header tag ad code end -->

    <!-- Buy sellads CSS-->
    <style>
        .pgAdWrapper {
          min-height: 0!important;
        }
        #carbonads{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",Helvetica,Arial,sans-serif;--width:728px;--font-size:22px}#carbonads{display:block;overflow:hidden;max-width:var(--width);position:relative;background-color:#fcfcfc;border:solid 1px #eee;font-size:var(--font-size);box-sizing:border-box;margin:36px 0 36px 0;max-height:90px}.detail #carbonads{margin-top:12px}#carbonads a{color:inherit;text-decoration:none}#carbonads a:hover{color:inherit}.carbon-wrap{display:flex;align-items:center}carbon-img{display:block;float:left;margin:0;max-width:var(--width);line-height:1}.carbon-img img{display:block;margin:0;height:90px;width:auto}.carbon-text{display:block;float:left;padding:0 1em;line-height:1.35;max-width:calc(100% - 130px - 2em);text-align:left}.carbon-poweredby{display:block;position:absolute;bottom:0;right:0;padding:6px 10px;background:repeating-linear-gradient(-45deg,transparent,transparent 5px,hsla(0,0%,0%,.025) 5px,hsla(0,0%,0%,.025) 10px) hsla(203,11%,95%,.8);text-align:center;text-transform:uppercase;letter-spacing:.5px;font-weight:601;font-size:8px;border-top-left-radius:4px;line-height:1}@media only screen and (min-width:320px) and (max-width:759px){.carbon-text{font-size:14px}}
     </style>

    <!-- Generated using https://dns-prefetch-generator.github.io/ -->
    <meta http-equiv="x-dns-prefetch-control" content="on" />
    <link rel="dns-prefetch" href="//www.googletagservices.com" />
    <link rel="dns-prefetch" href="//www.google-analytics.com" />
    <link rel="dns-prefetch" href="//c.amazon-adsystem.com" />
    <link rel="dns-prefetch" href="//dsh7ky7308k4b.cloudfront.net" />
    <link rel="dns-prefetch" href="//securepubads.g.doubleclick.net" />
    <link rel="dns-prefetch" href="//adservice.google.com" />
    <link rel="dns-prefetch" href="//cdnjs.cloudflare.com" />
    <link rel="dns-prefetch" href="//www.googletagmanager.com" />

    <link rel="stylesheet" href="playground.css?v=1fsaf" />
    <!-- Global site tag (gtag.js) - Google Analytics -->

  </head>

  <body>
    <!-- <select id="language-changer"></select> -->
    <div class="container" id="root" data-lang="python">
      <div class="spinner">
        <div class="loader"><span>{</span><span>}</span></div>
      </div>
      <div class="mobile-nav-drawer">
        <div class="nav-backdrop">
        </div>
        <div class="nav-menu">
          <div class="nav-header-wrapper">
              <div class="nav-logo-title-wrapper">
                <a href="https://www.programiz.com/" target="_blank" class="nav-logo-link" >
                  <img id="nav-logo" src="assets/logos/logo.svg" />
                </a>
              </div>
            <button type="button" class="close-nav-btn" title="Close navigation">
              <img class="svg" src="assets/icons/close.svg" />
            </button>
          </div>
          <div class="nav-menu-list">
            <a
              target="_blank"
              href="https://www.programiz.com/python-programming/online-compiler/"
              class="change-lang-row python active"
              title="Python Online Compiler"
            >
              <span class="change-lang-btn">
                <img
                  class="change-lang-btn-icon svg"
                  src="assets/icons/python.svg"
                />
              </span>
              <span class="nav-menu-text">
                Python Online Compiler
              </span>
            </a>
            <a
              target="_blank"
              href="https://www.programiz.com/c-programming/online-compiler/"
              class="change-lang-row c "
              title="C Online Compiler"
            >
              <span class="change-lang-btn">
                <img
                  class="change-lang-btn-icon svg"
                  src="assets/icons/c.svg"
                />
              </span>
              <span class="nav-menu-text">
                C Online Compiler
              </span>
            </a>
            <a
              target="_blank"
              href="https://www.programiz.com/cpp-programming/online-compiler/"
              class="change-lang-row cpp "
              title="C++ Online Compiler"
            >
              <span class="change-lang-btn">
                <img
                  class="change-lang-btn-icon svg"
                  src="assets/icons/cpp.svg"
                />
              </span>
              <span class="nav-menu-text">
                C++ Online Compiler
              </span>
            </a>
            <a
              target="_blank"
              href="https://www.programiz.com/java-programming/online-compiler/"
              class="change-lang-row java "
              title="Java Online Compiler"
            >
              <span class="change-lang-btn">
                <img
                  class="change-lang-btn-icon svg"
                  src="assets/icons/java.svg"
                />
              </span>
              <span class="nav-menu-text">
                Java Online Compiler
              </span>
            </a>
            <a
              target="_blank"
              href="https://www.programiz.com/csharp-programming/online-compiler/"
              class="change-lang-row csharp "
              title="C# Online Compiler"
            >
              <span class="change-lang-btn">
                <img
                  class="change-lang-btn-icon svg"
                  src="assets/icons/csharp.svg"
                />
              </span>
              <span class="nav-menu-text">
                C# Online Compiler
              </span>
            </a>
            <a
              target="_blank"
              href="https://www.programiz.com/javascript/online-compiler/"
              class="change-lang-row javascript "
              title="JavaScript Online Compiler (Editor)"
            >
              <span class="change-lang-btn">
                <img
                  class="change-lang-btn-icon svg"
                  src="assets/icons/javascript.svg"
                />
              </span>
              <span class="nav-menu-text">
                JavaScript Online Compiler
              </span>
            </a>
          </div>
        </div>
      </div>

      <div class="wrapper">
                <div class="header">
          <div class="header-wrapper">
            <div class="burger-menu">
              <button type="button" class="burger-menu-btn" title="Open navigation">
                <img class="svg burger-menu-btn-icon" src="assets/icons/burger.svg" />
              </button>
            </div>
            <div class="logo-wrapper">
              <h1 class="logo-title-wrapper">
                <a href="https://www.programiz.com/" target="_blank" class="logo-link" >
                  <img id="logo" src="assets/logos/logo.svg" />
                  <span class="logo-sub-title-wrapper">
                    <span class="logo-sub-title">Python Online Compiler</span>
                  </span>
                </a>
              </h1>
            </div>
          </div>
          <div class="compiler-header-ad">
            <div id="div-gpt-ad-Programizcom36786" class="content-top-ad">
            </div>

            <!-- buysell ads -->
                <div class="compiler-header-ad" id="carbon-block"></div>

          </div>
          <div id="add-replacement"></div>
          <div id="feedback-desktop">
            <a id="ad-link"
              >&nbsp;Learn Python App</a
            >
          </div>
          <div id="feedback-mobile">
            <a id="mobile-ad-link"
              >&nbsp;Learn Python</a>
          </div>
        </div>
        <div class="mobile-top-bar clearfix">
          <div class="options-wrapper">
            <div id="back-button" class="options-item-wrapper clearfix">
              <img class="svg options-item" src="assets/icons/back-arrow.svg" />
            </div>
          </div>
          <div class="pills-wrapper">
            <div class="pills clearfix">
              <button class="pill active compiler-pill">
                main.py              </button>
              <button class="pill shell-pill">
                Shell              </button>
            </div>
          </div>
          <div class="other-options-wrapper">
            <!-- <div id="feedback-mobile" class="options-item-wrapper">
              <a href="https://programiz.com/contact" class="options-item">
                <img class="svg" src="assets/icons/message-square.svg" />
              </a>
            </div> -->
            <div
              id="toggle-dark-mode-mobile"
              class="options-item-wrapper clearfix"
            >
              <img
                class="toggle-dark-mode-mobile-icon moon svg options-item"
                src="assets/icons/moon.svg"
              />
              <img
                class="toggle-dark-mode-mobile-icon sun svg options-item"
                src="assets/icons/sun.svg"
              />
            </div>
          </div>
        </div>
        <div class="sidebar-wrapper">
          <a
            target="_blank"
            href="https://www.programiz.com/python-programming/online-compiler/"
            class="change-lang-btn python active"
            title="Online Python Compiler"
          >
            <img
              class="change-lang-btn-icon svg"
              src="assets/icons/python.svg"
            />
          </a>
          <a
            target="_blank"
            href="https://www.programiz.com/c-programming/online-compiler/"
            class="change-lang-btn c "
            title="Online C Compiler"
          >
            <img
              class="change-lang-btn-icon svg"
              src="assets/icons/c.svg"
            />
          </a>
          <a
            target="_blank"
            href="https://www.programiz.com/cpp-programming/online-compiler/"
            class="change-lang-btn cpp "
            title="Online C++ Compiler"
          >
            <img
              class="change-lang-btn-icon svg"
              src="assets/icons/cpp.svg"
            />
          </a>
          <a
            target="_blank"
            href="https://www.programiz.com/java-programming/online-compiler/"
            class="change-lang-btn java "
            title="Online Java Compiler"
          >
            <img
              class="change-lang-btn-icon svg"
              src="assets/icons/java.svg"
            />
          </a>
          <a
            target="_blank"
            href="https://www.programiz.com/csharp-programming/online-compiler/"
            class="change-lang-btn csharp "
            title="Online C# Compiler"
          >
            <img
              class="change-lang-btn-icon svg"
              src="assets/icons/csharp.svg"
            />
          </a>
          <a
            target="_blank"
            href="https://www.programiz.com/javascript/online-compiler/"
            class="change-lang-btn javascript "
            title="Online JavaScript Compiler (Editor)"
          >
            <img
              class="change-lang-btn-icon svg"
              src="assets/icons/javascript.svg"
            />
          </a>
        </div>
        <div class="editor-wrapper">
          <div class="editor-desktop-top-bar">
            <div class="file-name">main.py</div>
            <div class="desktop-top-bar__btn-wrapper">
              <button
                type="button"
                id="toggle-expanded-mode-desktop"
                title="Enter Fullscreen"
              >
                <img
                  class="toggle-expanded-mode-mobile-icon expand svg"
                  src="assets/icons/expand.svg"
                />
                <img
                  class="toggle-expanded-mode-mobile-icon minimize hidden svg"
                  src="assets/icons/minimize.svg"
                />
              </button>
              <button type="button" id="toggle-dark-mode-desktop" title="Toggle dark mode">
                <img
                  class="toggle-dark-mode-mobile-icon moon svg"
                  src="assets/icons/moon.svg"
                />
                <img
                  class="toggle-dark-mode-mobile-icon sun svg"
                  src="assets/icons/sun.svg"
                />
              </button>
              <button class="desktop-run-button run">
                &nbsp;Run&nbsp;
              </button>
            </div>
          </div>
          <button class="mobile-run-button run">
            Run
          </button>
          <div id="editor"># Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")</div>
        </div>

        <div class="terminal-wrapper">
          <div class="terminal-desktop-top-bar">
            <div class="shell-name">
              Shell            </div>
            <div class="terminal-desktop-top-bar__btn-wrapper">
              <button class="desktop-clear-button">
                  &nbsp;Clear&nbsp;
              </button>
            </div>
          </div>
          <div id="terminal"></div>
        </div>
      </div>
    </div>

    <script defer type="text/javascript">

      var playStoreUrl =
          "https://play.google.com/store/apps/details?id=com.programiz.learnpython",
        appStoreUrl =
          "https://apps.apple.com/app/apple-store/id1472188189?pt=120228772",
        desktopUrl = "https://www.programiz.com/learn-python";

      var os, a;

      a = document.getElementById("ad-link");
      b = document.getElementById("mobile-ad-link");

      var lang = "python";
      var href = "https://app.programiz.com/app-compiler";
      var app = "Python";

      if(lang == 'c') {
        href = "https://learncprogramiz.page.link/app-compiler";
        app = "C";
      } else if(lang == 'java') {
        href = "https://learnjavaprogramiz.page.link/app-compiler";
        app = "Java";
      }

      a.innerHTML = `Learn ${app} App`;
      b.innerHTML = `Learn ${app}`;
      a.href = href;
      b.href = href;
    </script>
    <!-- The use of the cloudflare cdn for all external libraries is intential. We are trying to reduce the number
         of DNS lookups.
    -->
    <script
      defer
      src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/1.4.5/socket.io.min.js"
    ></script>
    <script
      defer
      src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.0/jquery.min.js"
    ></script>

    <script
      defer
      src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.11/ace.js"
    ></script>
    <script defer src="https://cdnjs.cloudflare.com/ajax/libs/mousetrap/1.4.6/mousetrap.min.js"></script>
    <script defer src="build/final.js?v=resize-fixv3"></script>
    <script
      defer
      src="https://www.googletagmanager.com/gtag/js?id=UA-36675496-1"
    ></script>
    <script defer>
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("js", new Date());

      gtag("config", "UA-36675496-1");
    </script>
  </body>
</html>
