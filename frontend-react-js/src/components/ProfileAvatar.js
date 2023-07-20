export default function ProfileAvatar(props) {
  const backgroundImage = `url("https://assets.crudder.click/avatars/${props.id}.jpg")`;
  const styles = {
    backgroundImage: backgroundImage,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    minWidth: '60px',
    minHeight: '60px', 
    borderRadius: '999px'
  };

  return (
    <div 
      className="profile-avatar"
      style={styles}
    ></div>
  );
}
