<script lang="ts">
	import { goto } from '$app/navigation';
    import type { PageProps } from './$types';
    import { MapLibre, GeoJSONSource, LineLayer } from 'svelte-maplibre-gl';
    let { data }: PageProps = $props();
    let pipes = data.pipes;
    let cursor: string | undefined = $state();
    
    function checkoutById(id: any) {
        goto(`/pipes/${id}`)
    }
</script>

<h1> Pipes </h1>

<MapLibre
    class="map-container"
    style="https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json"
    bounds={pipes.bbox}
    {cursor}
>
    <GeoJSONSource data={pipes}>
        <LineLayer
            onclick={(e) => checkoutById(e.features![0].id)}
            onmousemove={() => (cursor = "pointer")}
            onmouseleave={() => (cursor = undefined)}
            paint={{ 'line-width': 5.0, 'line-color': "#36F" }}
        />
    </GeoJSONSource>
</MapLibre>

<pre>{JSON.stringify(data, null, 2)}</pre>
