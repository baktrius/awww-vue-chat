<template>
  <div>
    <v-progress-circular
      v-if="loading"
      indeterminate
      color="primary"
    ></v-progress-circular>
    <div v-else>
      {{ value }}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      value: "",
      loading: false,
    };
  },
  mounted() {
    this.loading = true;
    fetch(this.url)
      .then((response) => response.text())
      .then((text) => {
        this.value = text;
        this.loading = false;
      });
  },
  props: {
    url: String,
  },
};
</script>
