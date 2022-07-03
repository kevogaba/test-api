import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles((theme) => ({
    cardMedia: {
        paddingTop: '56.25%', //16:9
    },
    link: {
        margin: theme.spacing(1, 1.5),
    },
    cardHeader: {
        backgroundColor:
            theme.palette.type === 'light'
                ? theme.palette.grey[200]
                : theme.palette.grey[700],
    },
    postTitle: {
        fontSize: '16px',
        textAlign: 'left',
    },
    postText: {
        display: 'flex',
        justifyContent: 'left',
        alignItems: 'baseline',
        fontSize: '12px',
        textAlign: 'left',
        marginBottom: theme.spacing(2),
    },
}));

const Accomplishment = (props) => {
    const { accomplishments } = props;
    const classes = useStyles();
    if (!accomplishments || accomplishments.length === 0)
        return <p> We cannot find any items, Sorry!! </p>;
    return (
        <React.Fragment>
            <Container maxWidth='md' component='main'>
                <Grid container spacing={5} alignItems='flex-end'>
                    {accomplishments.map((accomplishment) => {
                        return (
                            <Grid item key={accomplishment.id} xs={12} md={4}>
                                <Card className={classes.card}>
                                    <CardMedia
                                        className={classes.cardMedia}
                                        title="image title"
                                    />
                                    <CardContent className={classes.CardContent}>
                                        <Typography 
                                            gutterBottom
                                            variant='h6'
                                            component='h2'
                                            className={classes.postTitle}
                                        >
                                            {accomplishment.title.substr(0, 50)}...
                                        </Typography>
                                        <div className={classes.postText}>
                                            <Typography
                                                component="p"
                                                color="textPrimary">
                                            </Typography>
                                            <Typography variant="p" color="textSecondary">
                                                {accomplishment.accomplishment.substr(0, 60)}...
                                            </Typography>
                                        </div>
                                    </CardContent>
                                </Card>
                            </Grid>
                        );
                    })}
                </Grid>
            </Container>
        </React.Fragment>
    )
}

export default Accomplishment;
