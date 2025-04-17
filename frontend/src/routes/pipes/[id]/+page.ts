import type { PageLoad } from './$types';
import { PUBLIC_API_ENDPOINT } from '$env/static/public';

export const load: PageLoad = async ({ params, fetch }) => {
	const pipe = await(await fetch(`${PUBLIC_API_ENDPOINT}/pipes/${params.id}`)).json()
	return { pipe }
};
