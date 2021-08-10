import React, { Component } from "react";
import { TextField, Button, Grid, Typography } from "@material-ui/core";
import { Link } from "react-router-dom";

export default class RoomJoinPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            roomCode: "",
            error: "",
        }
    }

    render() {
        return (
            <Grid container spacing={1} alignItems="center">
                <Grid item xs={12} align="center">
                    <Typography component="h4" variant="h4">
                        Join a Room
                    </Typography>
                </Grid>
                <Grid item xs={12}align="center">
                    <TextField 
                        error={this.state.error.length > 0} 
                        label="Code" 
                        placeholder="Enter a Room Code" 
                        value={this.state.roomCode} 
                        helperText={this.state.error} 
                        variant="outlined"
                        onChange
                    />
                </Grid>
                <Grid item xs={12}align="center">
                <Button color="primary" variant="contained" onClick>Enter Room</Button>
                </Grid>
                <Grid item xs={12}align="center">
                <Button color="secondary" variant="contained" to="/" component={Link}>Back</Button>
                </Grid>
            </Grid>
        );
    }
    
}
