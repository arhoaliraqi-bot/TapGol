// services/profileService.js
import api from './api';

class ProfileService {
  async getCurrentProfile() {
    const response = await api.get('/profiles/current');
    return response.data;
  }

  async getUserProfile(userId) {
    const response = await api.get(`/profiles/${userId}`);
    return response.data;
  }

  async updateProfile(data) {
    const response = await api.put('/profiles/current', data);
    return response.data;
  }

  async followUser(userId) {
    const response = await api.post(`/profiles/${userId}/follow`);
    return response.data;
  }

  async unfollowUser(userId) {
    const response = await api.post(`/profiles/${userId}/unfollow`);
    return response.data;
  }
}

export default new ProfileService();
