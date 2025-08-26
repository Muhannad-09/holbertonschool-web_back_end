import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const queue = [];

  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPromise = uploadPhoto(fileName);

  const results = await Promise.allSettled([signUpPromise, uploadPromise]);

  results.forEach(result => {
    if (result.status === 'fulfilled') {
      queue.push({ status: 'fulfilled', value: result.value });
    } else {
      queue.push({ status: 'rejected', reason: result.reason });
    }
  });

  return queue;
}
