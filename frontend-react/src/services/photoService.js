// services/photoService.js
import api from './api';

class PhotoService {
  async uploadPhoto(file, metadata = {}) {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('title', metadata.title || '');
    formData.append('description', metadata.description || '');
    
    if (metadata.matchId) formData.append('match_id', metadata.matchId);
    if (metadata.groupId) formData.append('group_id', metadata.groupId);
    if (metadata.isProfilePicture) formData.append('is_profile_picture', true);

    const response = await api.post('/uploads/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    return response.data;
  }

  async getUserPhotos() {
    const response = await api.get('/uploads/user/photos');
    return response.data;
  }

  async getMatchPhotos(matchId) {
    const response = await api.get(`/uploads/match/${matchId}/photos`);
    return response.data;
  }

  async getGroupPhotos(groupId) {
    const response = await api.get(`/uploads/group/${groupId}/photos`);
    return response.data;
  }

  async updatePhoto(photoId, data) {
    const response = await api.put(`/uploads/${photoId}`, data);
    return response.data;
  }

  async deletePhoto(photoId) {
    const response = await api.delete(`/uploads/${photoId}`);
    return response.data;
  }
}

export default new PhotoService();
