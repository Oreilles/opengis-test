import type { PageLoad } from './$types';
import { PUBLIC_API_ENDPOINT } from '$env/static/public';
import { bbox } from '@turf/turf';

export const load: PageLoad = async ({ fetch }) => {
	const pipes = await (await fetch(`${PUBLIC_API_ENDPOINT}/pipes`)).json()
    pipes.bbox = bbox(pipes)
	return { pipes }
};
