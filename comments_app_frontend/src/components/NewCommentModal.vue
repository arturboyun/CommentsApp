<template>
  <transition name="modal">
    <div class="modal_mask">
      <div class="modal_container">

        <div class="modal_header">
          <h2>New comment</h2>
          <button class="close_modal_btn" @click="$emit('close')">
            <img src="@/assets/icons/x.svg" alt="">
          </button>
        </div>

        <div class="modal__reply_to" v-if="replyToID">
          <div class="reply_to__content">
            <div class="reply_to__text">{{ replyToComment.username }}</div>
            <img class="reply_to__icon" src="@/assets/icons/answer_arrow.svg" alt="">
          </div>
        </div>

        <form @submit.prevent="onSubmit">
          <div class="modal_body">

            <label for="username">User name<span>*</span></label>
            <input type="text"
                   name="username"
                   id="username"
                   v-model.trim="$v.username.$model"
                   :class="{'invalid': ($v.username.$dirty && !$v.username.required) || ($v.username.$dirty && !$v.username.minLength)}"
            >
            <div class="error" v-if="$v.username.$dirty && !$v.username.required">Field is required</div>
            <div class="error" v-else-if="$v.username.$dirty && !$v.username.minLength">
              User name must have at least {{ $v.username.$params.minLength.min }} letters.
            </div>

            <label for="email">E-mail<span>*</span></label>
            <input type="text"
                   name="email"
                   id="email"
                   v-model.trim="$v.email.$model"
                   :class="{'invalid': ($v.email.$dirty && !$v.email.required) || ($v.email.$dirty && !$v.email.email)}"
            >
            <div class="error" v-if="$v.email.$dirty && !$v.email.required">Field is required</div>
            <div class="error" v-else-if="$v.email.$dirty && !$v.email.email">Email must be like example@gmail.com</div>

            <label for="homepage">Home page</label>
            <input type="text"
                   name="homepage"
                   id="homepage"
            >

            <label for="text">Text<span>*</span></label>
            <textarea name="text"
                      id="text"
                      cols="30"
                      rows="5"
                      v-model.trim="$v.text.$model"
                      :class="{'invalid': ($v.username.$dirty && !$v.text.required) || ($v.username.$dirty && !$v.username.text)}"
            />
            <div class="error" v-if="$v.text.$dirty && !$v.text.required">Field is required</div>
            <div class="error" v-else-if="$v.text.$dirty && !$v.text.minLength">
              User name must have at least {{ $v.text.$params.minLength.min }} letters.
            </div>

            <div class="recaptcha">
              <vue-recaptcha
                  ref="recaptcha"
                  @verify="onVerify"
                  @expired="onExpired"
                  :sitekey="site_key"/>
            </div>
          </div>
          <div class="modal_footer">
            <button type="submit" :disabled="submitDisabled">Отправить</button>
          </div>
        </form>
      </div>
    </div>
  </transition>
</template>

<script>
import VueRecaptcha from 'vue-recaptcha';
import {email, required, minLength} from "vuelidate/lib/validators";

export default {
  name: "NewCommentModal",
  components: {VueRecaptcha},
  props: {
    replyToID: {
      type: Number,
      default: 0
    }
  },
  data: () => ({
    replyToComment: {},
    site_key: "6LdSK9gZAAAAALwDlrxgBniqMD6t86_dtNKuXEWl",
    submitDisabled: true,
    username: '',
    email: '',
    homepage: '',
    text: '',
  }),
  validations: {
    username: {required, minLength: minLength(2)},
    email: {required, email},
    text: {required, minLength: minLength(5, 200)}
  },
  async created() {
    this.replyToComment = await this.$store.dispatch('getComment', this.replyToID)
  },
  methods: {
    async onSubmit() {
      if (this.$v.$invalid) {
        this.$v.$touch()
        return
      }
      const data = {
        username: this.username,
        email: this.email,
        homepage: this.homepage,
        text: this.text,
        reply_to: this.replyToID
      }
      const isSuccess = await this.createComment(data)
      if (isSuccess)
        this.$noty.success("Your comment has been saved!")
      else
        this.$noty.error("Oops, something went wrong! Try again :)")
      this.$emit('close')
    },
    onVerify() {
      this.submitDisabled = false
    },
    onExpired() {
      this.submitDisabled = true
    },
    async createComment(data) {
      return await this.$store.dispatch('createComment', data)
    }
  }
}
</script>

<style lang="scss" scoped>
@import '~vuejs-noty/dist/vuejs-noty.css';

.modal-enter, .modal-leave-to {
  opacity: 0;
}

.modal-enter-active, .fade-leave-active {
  transition: .5s ease;
}

.modal_mask {
  position: fixed;
  z-index: 100;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: 0.3s ease;
  overflow: hidden;
}

.modal_container {
  display: flex;
  flex-direction: column;
  width: 310px;
  padding: 15px;
  background-color: #fff;
  border-radius: 15px;
  box-shadow: 0 15px 50px 0 rgba(0, 0, 0, .25);
  transition: all 0.3s ease;
  overflow-y: auto;

  @media screen and (max-width: 768px) {
    width: 100%;
    min-height: 100vh;
    padding-top: 115px;
  }
}

.modal__reply_to {
  display: flex;
  align-items: center;
  margin-bottom: 15px;

  .reply_to__content {
    display: flex;
    align-items: center;
    padding: 5px 8px;
    background-color: var(--accent-color);
    border-radius: 5px;

    .reply_to__text {
      color: #ffffff;
      font-weight: 600;
      margin-right: 8px;
    }

    .reply_to__icon {
      width: 22px;
      height: 22px;
    }
  }
}

.modal_header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 15px;

  h2 {
    margin: 0;
  }

  .close_modal_btn {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0;
    padding: 0;
    background-color: #fff;
    cursor: pointer;
    border: none;
  }
}

.modal_body {
  display: flex;
  flex-direction: column;

  label {
    color: var(--grey-color);
    margin-top: 10px;
    margin-bottom: 4px;

    &:first-child {
      margin-top: 0;
    }

    span {
      color: var(--danger-color);
    }
  }

  input, textarea {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    display: flex;
    padding: 10px;
    color: var(--black-color);
    font-size: 14px;
    line-height: 14px;
    border-radius: 5px;
    border: 1px solid var(--primary-color);
    background-color: #EEF7FF;
    transition: .2s ease;
  }

  input:focus, textarea:focus {
    color: var(--black-color);
    border: 1px solid var(--accent-color);
    -webkit-overflow-scrolling: touch;
    -webkit-transform: translateZ(0px)
  }

  input.invalid {
    border: 1px solid var(--danger-color);
  }

  .error {
    font-size: 12px;
    color: var(--danger-color);
    margin-top: 5px;
  }

  textarea {
    resize: vertical;
  }

  .recaptcha {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    margin-top: 10px;
    margin-bottom: 10px;
  }
}

.modal_footer {
  display: flex;
  align-items: center;
  justify-content: center;

  button {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    line-height: 14px;
    width: 100%;
    height: 38px;
    color: #fff;
    border-radius: 5px;
    border: 1px solid var(--primary-color);
    background-color: var(--accent-color);
    cursor: pointer;
    transition: .5s ease;
  }

  button[disabled] {
    color: #595959;
    background-color: #DBDBDB;
    border: 1px solid #595959;
    cursor: default;
  }
}
</style>