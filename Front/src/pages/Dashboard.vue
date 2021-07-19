<template>
<div align="center">

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
<br clear = right>
<br clear = right>
<br clear = right>
<br clear = right>
<br clear = right>
<br clear = right>
<br clear = right>
<br clear = right>
<br clear = right>
    <div align="right">
    </div>     
</div>
<footer class="footer">
      <nav>
        <ul>
          <li>
            <a href="" target="_blank">Profesionales</a>
          </li>
          <li>
            <a href="" target="_blank">
              Beneficio
            </a>
          </li>
          <li>
            <a href="" target="_blank">
              Contáctanos
            </a>
          </li>
          <li>
              <router-link 
                      :to="{ name: 'quienessomos' }"
                     
                      >¿Quienes Somos?</router-link>
          </li>
        </ul>
      </nav>
      <img style="max-width:200px;width:auto;height:auto;" src="@/assets/img/logo color horizontal.png">
  </footer>
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
