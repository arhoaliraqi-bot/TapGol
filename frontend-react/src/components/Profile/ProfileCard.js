// components/Profile/ProfileCard.js
import React, { useState, useEffect } from 'react';
import profileService from '../../services/profileService';
import './ProfileCard.css';

const ProfileCard = ({ userId, isCurrentUser = false }) => {
  const [profile, setProfile] = useState(null);
  const [isFollowing, setIsFollowing] = useState(false);
  const [loading, setLoading] = useState(true);
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    loadProfile();
  }, [userId]);

  const loadProfile = async () => {
    try {
      setLoading(true);
      const data = userId 
        ? await profileService.getUserProfile(userId)
        : await profileService.getCurrentProfile();
      setProfile(data);
    } catch (error) {
      console.error('Error loading profile:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleUpdateProfile = async (updatedData) => {
    try {
      await profileService.updateProfile(updatedData);
      loadProfile();
      setIsEditing(false);
    } catch (error) {
      console.error('Error updating profile:', error);
    }
  };

  const handleFollowToggle = async () => {
    try {
      if (isFollowing) {
        await profileService.unfollowUser(userId);
      } else {
        await profileService.followUser(userId);
      }
      setIsFollowing(!isFollowing);
    } catch (error) {
      console.error('Error toggling follow:', error);
    }
  };

  if (loading) return <div className="loading">Loading...</div>;
  if (!profile) return <div className="error">Profile not found</div>;

  return (
    <div className="profile-card">
      <div className="profile-header">
        <img 
          src={profile.profile_picture || '/default-avatar.png'}
          alt={profile.name}
          className="profile-picture"
        />
        <div className="profile-info">
          <h2>{profile.name}</h2>
          <p className="username">@{profile.username}</p>
          <p className="bio">{profile.bio}</p>
        </div>
      </div>

      <div className="profile-stats">
        <div className="stat">
          <strong>Followers</strong>
          <span>{profile.followers_count || 0}</span>
        </div>
        <div className="stat">
          <strong>Following</strong>
          <span>{profile.following_count || 0}</span>
        </div>
      </div>

      <div className="profile-actions">
        {isCurrentUser ? (
          <button 
            className="edit-btn"
            onClick={() => setIsEditing(!isEditing)}
          >
            {isEditing ? 'Cancel' : 'Edit Profile'}
          </button>
        ) : (
          <button 
            className={`follow-btn ${isFollowing ? 'following' : ''}`}
            onClick={handleFollowToggle}
          >
            {isFollowing ? 'Following' : 'Follow'}
          </button>
        )}
      </div>

      {isEditing && isCurrentUser && (
        <ProfileEditor profile={profile} onSave={handleUpdateProfile} />
      )}
    </div>
  );
};

const ProfileEditor = ({ profile, onSave }) => {
  const [formData, setFormData] = useState({
    name: profile.name,
    bio: profile.bio || '',
    profile_picture: profile.profile_picture || ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave(formData);
  };

  return (
    <form className="profile-editor" onSubmit={handleSubmit}>
      <div className="form-group">
        <label>Name</label>
        <input 
          type="text" 
          name="name" 
          value={formData.name}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <label>Bio</label>
        <textarea 
          name="bio" 
          value={formData.bio}
          onChange={handleChange}
          placeholder="Tell us about yourself"
        />
      </div>
      <div className="form-group">
        <label>Profile Picture URL</label>
        <input 
          type="text" 
          name="profile_picture" 
          value={formData.profile_picture}
          onChange={handleChange}
          placeholder="https://example.com/image.jpg"
        />
      </div>
      <button type="submit" className="save-btn">Save Changes</button>
    </form>
  );
};

export default ProfileCard;
