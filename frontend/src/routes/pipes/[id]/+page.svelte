<script lang="ts">
    import type { PageProps } from './$types';
    import { GeoJSONSource, LineLayer, MapLibre } from 'svelte-maplibre-gl';
    let { data }: PageProps = $props();
    let pipe = data.pipe;
</script>
  
<h1> Pipe #{pipe.id} </h1>

<MapLibre
    class="map-container"
    style="https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json"
    bounds={pipe.bbox}
>
    <GeoJSONSource data={pipe}>
        <LineLayer paint={{ 'line-width': 5.0, 'line-color': "#36F" }} />
    </GeoJSONSource>
</MapLibre>

<pre>{JSON.stringify(data, null, 2)}</pre>
