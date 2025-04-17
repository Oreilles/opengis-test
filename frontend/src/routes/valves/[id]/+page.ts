import type { PageLoad } from './$types';
import { PUBLIC_API_ENDPOINT } from '$env/static/public';

export const load: PageLoad = async ({ params, fetch }) => {
	const valve = await (await fetch(`${PUBLIC_API_ENDPOINT}/valves/${params.id}`)).json()
	return { valve }
};
