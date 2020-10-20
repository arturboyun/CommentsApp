<template>
  <div id="app">

    <h1 class="header">Comments App</h1>

    <router-view @answer-to="showAnswerTo"/>

    <button class="new_comment_modal" @click="showNewComment">
      <img src="@/assets/icons/plus_icon.svg" alt="">
    </button>

    <NewCommentModal
        v-if="showNewCommentModal"
        @close="showNewCommentModal = false"
        :replyToID="replyToID"
    />
  </div>
</template>

<script>
import NewCommentModal from "@/components/NewCommentModal"

export default {
  components: {NewCommentModal},
  data() {
    return {
      replyToID: 0,
      showNewCommentModal: false,
    }
  },
  methods: {
    showNewComment() {
      this.replyToID = null
      this.showNewCommentModal = true
      this.showNewCommentModal = true
    },
    showAnswerTo(id) {
      this.replyToID = id
      this.showNewCommentModal = true
    }
  }
}
</script>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap');

  :root {
    --primary-color: #C2DBF2;
    --black-color: #151515;
    --grey-color: #777777;
    --accent-color: #3eafee;
    --danger-color: #ec4141;
  }

  body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    background-color: var(--primary-color);
    font-family: 'Montserrat', sans-serif;
    font-size: 15px;
    width: 100%;
  }

  a {
    color: var(--grey-color);
    text-decoration: none;
    transition: .5s ease;

    &:hover {
      color: var(--accent-color);
    }
  }

  input, button, textarea {
    font-family: 'Montserrat', sans-serif;
    font-size: 15px;
    line-height: 15px;
    outline: none;
  }

  .header {
    margin-top: 18px;
    margin-bottom: 24px;
    font-size: 24px;
    font-weight: 900;
    line-height: 24px;
    text-align: center;
  }

  .new_comment_modal {
    position: fixed;
    bottom: 30px;
    right: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 14px;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    background-color: var(--accent-color);
    box-shadow: 0 5px 15px rgba(62, 175, 238, .8);
    transition: .3s ease;

    &:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 20px rgba(62, 175, 238, .4);
    }
  }
</style>
