document.addEventListener("DOMContentLoaded", function () {
    const sendMessageForm = document.getElementById("send-message-form");
    const userMessageInput = document.getElementById("user-message");
    const chatContainer = document.getElementById("chat-container");
  
    if (sendMessageForm) {
      sendMessageForm.addEventListener("submit", async function (e) {
        e.preventDefault();
        const message = userMessageInput.value.trim();
        if (!message) return;
        userMessageInput.value = "";
  
        // Display user's message in the chat box
        addMessageToUI("user", message);
  
        try {
          const formData = new FormData();
          formData.append("message", message);
  
          const response = await fetch("/send_message", {
            method: "POST",
            body: formData,
          });
          const data = await response.json();

          if (data.error) {
            addMessageToUI("error", data.error);
          } else {
            addMessageToUI("Assistant", data.message); // Display AI response with model name
          }
        } catch (error) {
          addMessageToUI("error", "Error sending message. Please try again.");
        }
      });
    }
  
    function addMessageToUI(role, message) {
      const messageRow = document.createElement("div");
      messageRow.classList.add("message-row", role);
  
      const messageContent = document.createElement("div");
      messageContent.classList.add("message-content");
      messageContent.textContent = `${role}: ${message}`;
  
      messageRow.appendChild(messageContent);
      chatContainer.appendChild(messageRow);
      chatContainer.scrollTop = chatContainer.scrollHeight;
    }
  });
  