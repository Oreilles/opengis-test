<script lang="ts">
	import { goto } from '$app/navigation';
    import type { PageProps } from './$types';
    import { GeoJSONSource, CircleLayer, MapLibre } from 'svelte-maplibre-gl';
    let { data }: PageProps = $props();
    let valves = data.valves;
    let cursor: string | undefined = $state();
    
    function checkoutById(id: any) {
        goto(`/valves/${id}`)
    }
</script>

<h1> Valves </h1>
  
<MapLibre
    class="map-container"
    style="https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json"
    bounds={valves.bbox}
    {cursor}
>
    <GeoJSONSource data={valves}>
        <CircleLayer
            onclick={(e) => checkoutById(e.features![0].id)}
            onmousemove={() => (cursor = "pointer")}
            onmouseleave={() => (cursor = undefined)}
            paint={{ 'circle-radius': 10.0, 'circle-color': "#36F" }}
        />
    </GeoJSONSource>
</MapLibre>

<pre>{JSON.stringify(data, null, 2)}</pre>
