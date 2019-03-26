
$(function() {


  function addParticipantsMessage (data) {
    // console.log("addParticipantsMessage");
    var message = '';
    if (data.numUsers === 1) {
      message += "1 participant online";
    } else {
      console.log(data);
      console.log(data.numUsers);
      message += data.numUsers + " jurors online";
    }
    log(message);
  }

  // Sets the client's username
  function setUsername () {
    username = $usernameInput.val();
    // username = cleanInput($usernameInput.val().trim());

    // If the username is valid
    if (username) {

      console.log('setting username', username);

      $loginPage.fadeOut();
      $chatPage.show();
      $loginPage.off('click');
      $currentInput = $inputMessage.focus();

      // Tell the server your username
      socket.emit('add user', username);

    }
  }

  // Sends a chat message
  function sendMessage () {
    console.log("sendMessage");
    var message = $inputMessage.val();
    // Prevent markup from being injected into the message
    // message = cleanInput(message);
    // if there is a non-empty message and a socket connection
    if (message && connected) {
      $inputMessage.val('');
      addChatMessage({
        username: username,
        message: message
      });
      // tell server to execute 'new message' and send along one parameter
      socket.emit('new message', message);
    }
  }

  // Log a message
  function log (message, options) {
    // console.log("log function");
    var $el = $("<li>").addClass('log').text(message);
    addMessageElement($el, options);
  }

  // Adds the visual chat message to the message list
  function addChatMessage (data, options) {
    // Don't fade the message in if there is an 'X was typing'
    var $typingMessages = getTypingMessages(data);
    options = options || {};
    if ($typingMessages.length !== 0) {
      options.fade = false;
      $typingMessages.remove();
    }

    var $usernameDiv = $('<span class="username"/>')
      .text(data.username)
      .css('color', getUsernameColor(data.username));
    var $messageBodyDiv = $('<span class="messageBody">')
      .text(data.message);

    var typingClass = data.typing ? 'typing' : '';
    var $messageDiv = $('<li class="message"/>')
      .data('username', data.username)
      .addClass(typingClass)
      .append($usernameDiv, " ", $messageBodyDiv);

    console.log("addChatMessage");
    addMessageElement($messageDiv, options);
  }

  // Adds the visual chat typing message
  function addChatTyping (data) {
    console.log("addChatTyping");
    data.typing = true;
    data.message = ' is typing';
    addChatMessage(data);
  }

  // Removes the visual chat typing message
  function removeChatTyping (data) {
    console.log("removeChatTyping");
    getTypingMessages(data).fadeOut(function () {
      $(this).remove();
    });
  }

  // Adds a message element to the messages and scrolls to the bottom
  // el - The element to add as a message
  // options.fade - If the element should fade-in (default = true)
  // options.prepend - If the element should prepend
  //   all other messages (default = false)
  function addMessageElement (el, options) {
    // console.log("addMessageElement");
    var $el = $(el);

    // Setup default options
    if (!options) {
      options = {};
    }
    if (typeof options.fade === 'undefined') {
      options.fade = true;
    }
    if (typeof options.prepend === 'undefined') {
      options.prepend = false;
    }

    // Apply options
    if (options.fade) {
      $el.hide().fadeIn(FADE_TIME);
    }
    if (options.prepend) {
      $messages.prepend($el);
    } else {
      $messages.append($el);
    }
    // console.log("message scroll to");

    var chatTop = $("#messages").scrollTop();
    var chatHeight = $("#messages").height();
    // console.log(chatHeight, chatTop);

    $("#messages").scrollTop($messages[0].scrollHeight);
  }

  // Prevents input from having injected markup
  function cleanInput (input) {
    console.log("cleanInput");
    return $('<div/>').text(input).html();
  }

  // Updates the typing event
  function updateTyping () {
    console.log("updateTyping");
    if (connected) {
      if (!typing) {
        typing = true;
        socket.emit('typing');
      }
      lastTypingTime = (new Date()).getTime();

      setTimeout(function () {
        var typingTimer = (new Date()).getTime();
        var timeDiff = typingTimer - lastTypingTime;
        if (timeDiff >= TYPING_TIMER_LENGTH && typing) {
          socket.emit('stop typing');
          typing = false;
        }
      }, TYPING_TIMER_LENGTH);
    }
  }

  // Gets the 'X is typing' messages of a user
  function getTypingMessages (data) {
    return $('.typing.message').filter(function (i) {
      return $(this).data('username') === data.username;
    });
  }

  // Gets the color of a username through our hash function
  function getUsernameColor (username) {
    // Compute hash code
    var hash = 7;
    for (var i = 0; i < username.length; i++) {
       hash = username.charCodeAt(i) + (hash << 5) - hash;
    }
    // Calculate color
    var index = Math.abs(hash % COLORS.length);
    return COLORS[index];
  }



  $inputMessage.on('input', function() {
    console.log("input message on input");
    updateTyping();
  });

  // Click events

  // Focus input when clicking anywhere on login page
  $loginPage.click(function () {
    $currentInput.focus();
  });

  // Focus input when clicking on the message input's border
  $inputMessage.click(function () {
    console.log("click input");
    $inputMessage.focus();
  });

  // Socket events

  // Whenever the server emits 'login', log the login message
  socket.on('login', function (data) {
    console.log("login");
    connected = true;
    // Display the welcome message
    var message = "Welcome! You can chat with other jurors here";
    log(message, {
      prepend: true
    });
    addParticipantsMessage(data);
  });

  // Whenever the server emits 'new message', update the chat body
  socket.on('new message', function (data) {
    addChatMessage(data);
  });

  // Whenever the server emits 'user joined', log it in the chat body
  socket.on('user joined', function (data) {
    log(data.username + ' joined');
    addParticipantsMessage(data);
  });

  socket.on('user left', function (data) {
    log(data.username + ' left');
  });

  // user_requested_help
  socket.on('user_requested_help', function (data) {

    log(data.username + ' needs help');

    console.log(data);
    addParticipantsMessage(data);
  });

  // Whenever the server emits 'typing', show the typing message
  socket.on('typing', function (data) {
    addChatTyping(data);
  });

  // Whenever the server emits 'stop typing', kill the typing message
  socket.on('stop typing', function (data) {
    removeChatTyping(data);
  });

  // update users
  socket.on('users', function (data) {
    console.log('users', data);

    var locations = [];
    for(var k in data) {
        var user = data[k]
        // if user data isn't you
        if (user.lat && user.lon && user.username != username) {
            // add other people to locations
            locations.push({
                coords: [user.lat, user.lon],
                name: user.username,
                status: user.status
            })
        }
    }

    console.log(locations);
    theMap.displayData = locations;
    console.log("UPDATE VIS from USERS broadcast");
    theMap.updateVis();
  });

  socket.on('disconnect', function () {
    log('you have been disconnected');
  });

  socket.on('reconnect', function () {
    log('you have been reconnected');
    if (username) {
      socket.emit('add user', username);
    }
  });

  socket.on('reconnect_error', function () {
    log('attempt to reconnect has failed');
  });

});
