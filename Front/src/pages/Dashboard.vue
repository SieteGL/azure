<template>


<div class="content" align="center">
  <hooper style="max-width:70%;width:auto;height:auto;" :progress="true" :autoPlay="true" :playSpeed="7000">
  <slide>
    <img style="max-width:70%;width:auto;height:auto;" src="@/assets/img/img1.jpg">
  </slide>
  <slide>
    <img style="max-width:70%;width:auto;height:auto;" src="@/assets/img/img2.jpg">
  </slide>
  <slide>
    <img style="max-width:70%;width:auto;height:auto;" src="@/assets/img/img3.jpg">
  </slide>
  <slide>
    <img style="max-width:70%;width:auto;height:auto;" src="@/assets/img/img4.jpg">
  </slide>
</hooper>
</div>
</template>

<script>
import { Hooper, Slide } from 'hooper';
import 'hooper/dist/hooper.css';

export default {
  name: 'App',
  components: {
    Hooper,
    Slide
  }
};
</script>
