<template>
  <v-list lines="three">
    <v-list-item
      v-for="(message, i) in paginatedMessages"
      :key="i"
      :title="message.title"
      :subtitle="message.subtitle"
      :prepend-avatar="'https://randomuser.me/api/portraits/women/8.jpg'"
    >
      <v-dialog max-width="500">
        <template v-slot:activator="{ props: activatorProps }">
          <v-btn
            v-bind="activatorProps"
            color="surface-variant"
            text="Show more"
            variant="flat"
          ></v-btn>
        </template>

        <template v-slot:default="{ isActive }">
          <v-card :title="message.title">
            <v-card-text>
              {{ message.subtitle }}
            </v-card-text>

            <v-divider></v-divider>

            <v-card-text>
              <SlowValue :url="'http://localhost:8000/slow'" />
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn text="Close" @click="isActive.value = false"></v-btn>
            </v-card-actions>
          </v-card>
        </template>
      </v-dialog>
    </v-list-item>
  </v-list>
  <v-pagination :length="pageTotal" v-model="pageNumber"></v-pagination>
  <v-textarea clearable label="Message" v-model="currentMessage"></v-textarea>
  <v-btn block @click="sendMessage">Send</v-btn>
</template>

<script>
export default {
  name: "HelloWorld",
  data: () => ({
    messages: [],
    currentMessage: "",
    pageNumber: 1,
  }),
  computed: {
    pageTotal() {
      return Math.ceil(this.messages.length / 4);
    },
    paginatedMessages() {
      const num = this.pageTotal - this.pageNumber;
      return this.messages.slice(num * 4, (num + 1) * 4);
    },
  },
  methods: {
    sendMessage() {
      this.ws.send(this.currentMessage);
      this.currentMessage = "";
    },
    onMessage(event) {
      this.messages.push({
        title: "Item 6",
        subtitle: event.data,
      });
    },
  },
  created() {
    this.ws = new WebSocket("ws://localhost:8000/ws");
    this.ws.onmessage = this.onMessage;
  },
};
</script>
