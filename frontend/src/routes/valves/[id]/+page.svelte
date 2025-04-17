<script lang="ts">
    import type { PageProps } from './$types';
    import { CircleLayer, GeoJSONSource, MapLibre } from 'svelte-maplibre-gl';
    let { data }: PageProps = $props();
    let valve = data.valve;
</script>
  
<h1> Valve #{valve.id} </h1>

<MapLibre
    class="map-container"
    style="https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json"
    center={valve.geometry.coordinates}
    zoom={10}
>
    <GeoJSONSource data={valve}>
        <CircleLayer paint={{ 'circle-radius': 10.0, 'circle-color': "#36F" }} />
    </GeoJSONSource>
</MapLibre>

<pre>{JSON.stringify(data, null, 2)}</pre>
