import type { PageLoad } from './$types';
import { PUBLIC_API_ENDPOINT } from '$env/static/public';
import { bbox } from '@turf/turf';

export const load: PageLoad = async ({ fetch }) => {
	const valves = await (await fetch(`${PUBLIC_API_ENDPOINT}/valves`)).json()
    valves.bbox = bbox(valves)
    return { valves }
};
