<template>
    <div id="nav">
        <EventCategory />
        <route-view/>
    </div>
    <router-view/>
</template>

<style lang="scss">

</style>

<script>
    import EventCategory from "./components/EventCategory";
    export default {
        components: {EventCategory}
    }
</script>