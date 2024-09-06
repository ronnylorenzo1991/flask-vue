<script setup>
import DataStatsComponent from '@/components/DataStats/DataStatsComponent.vue'

const props = defineProps({
  cardItems: {
    default: []
  },
})
</script>

<template>
  <DataStatsComponent :title="item.title" :label="item.label" :total="item.total" :icon="item.icon"
    :percent="item.percent" v-for="(item, index) in props.cardItems" :key="index" />
</template>
