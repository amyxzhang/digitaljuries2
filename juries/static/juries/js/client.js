console.log("load client.js");

$(function() {


  function addParticipantsMessage (data) {
    console.log("addParticipantsMessage");
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





  // Log a message
  function log (message, options) {
    // console.log("log function");
    var $el = $("<li>").addClass('log').text(message);
    addMessageElement($el, options);
  }



  // Adds the visual chat typing message
  function addChatTyping (data) {
    console.log("addChatTyping");
    data.typing = true;
    data.message = ' is typing';
    // Change title of page when someone is typing
    document.title = 'Someone is typing...';
    console.log("change typing title");
    addChatMessage(data);
  }

  // Removes the visual chat typing message
  function removeChatTyping (data) {
    console.log("removeChatTyping");
    getTypingMessages(data).fadeOut(function () {
      $(this).remove();
    });
    document.title = 'Digital Juries | Experiments with New Civic Models Online';
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



  // Keyboard events



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
